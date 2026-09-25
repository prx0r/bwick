/**
 * Card Renderer — Satori → SVG → resvg → PNG
 * 
 * Produces print-ready card files at 300 DPI.
 * Pipeline: template JSX → Satori SVG → resvg PNG → Sharp composite
 */
import satori from "satori";
import { Resvg } from "@resvg/resvg-js";
import sharp from "sharp";
import { readFileSync } from "fs";
import { join } from "path";

// A5 card at 300 DPI
const CARD = { w: 1748, h: 2480, bleed: 35, safe: 59 }; // 148mm x 210mm

// Load font (Inter TTF)
const fontDir = join(process.cwd(), "fonts");
const fontPath = join(fontDir, "Inter-Regular.ttf");
let fontData;
try { fontData = readFileSync(fontPath); } catch { fontData = null; }

const fontBoldPath = join(fontDir, "Inter-Bold.ttf");
let fontBoldData;
try { fontBoldData = readFileSync(fontBoldPath); } catch { fontBoldData = null; }

const fontBlackPath = join(fontDir, "Inter-Black.ttf");
let fontBlackData;
try { fontBlackData = readFileSync(fontBlackPath); } catch { fontBlackData = null; }

/**
 * Render a card to PNG
 * @param {Object} opts
 * @param {string} opts.setup - Headline text
 * @param {string} opts.punchline - Inside/punchline text
 * @param {string} opts.petImageBuffer - Pet photo as Buffer (optional)
 * @param {string} opts.roast - "mild" | "roast" | "savage"
 * @param {string} opts.side - "front" | "inside"
 * @returns {Buffer} PNG buffer
 */
export async function renderCard({ setup, punchline, petImageBuffer, roast = "roast", side = "front" }) {
  const color = roast === "savage" ? "#ff4444" : roast === "roast" ? "#ff8844" : "#44aaff";

  // Build the React-like JSX tree for Satori
  const jsx = {
    type: "div",
    props: {
      style: {
        width: CARD.w,
        height: CARD.h,
        background: "#1a1a2e",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: 60,
        fontFamily: "Inter",
        position: "relative",
        overflow: "hidden",
        color: "#fff",
      },
      children: [
        // Background gradient
        {
          type: "div",
          props: {
            style: {
              position: "absolute", top: -400, left: -400, width: CARD.w + 800, height: CARD.h + 800,
              background: `radial-gradient(circle at 30% 70%, rgba(255,107,107,0.15) 0%, transparent 50%),
                           radial-gradient(circle at 70% 30%, rgba(78,205,196,0.1) 0%, transparent 50%)`,
            },
          },
        },
        // Badge
        {
          type: "div",
          props: {
            style: {
              position: "absolute", top: 24, left: 32,
              background: `${color}22`, color: color,
              padding: "8px 16px", borderRadius: 24,
              fontSize: 11, fontWeight: 700, textTransform: "uppercase",
              letterSpacing: 1.5, zIndex: 1,
              display: "flex",
            },
            children: [roast],
          },
        },
        // Content
        {
          type: "div",
          props: {
            style: { position: "relative", zIndex: 1, textAlign: "center", maxWidth: "90%", display: "flex", flexDirection: "column", alignItems: "center" },
            children: [
              // Headline
              {
                type: "div",
                props: {
                  style: { fontSize: 42, fontWeight: 900, lineHeight: 1.15, marginBottom: 20, display: "flex" },
                  children: [setup || ""],
                },
              },
              // Pet photo or placeholder
              ...(petImageBuffer ? [{
                type: "img",
                props: {
                  src: `data:image/jpeg;base64,${petImageBuffer.toString("base64")}`,
                  style: {
                    width: 300, height: 300, borderRadius: "50%", objectFit: "cover",
                    border: "5px solid rgba(255,255,255,0.15)", margin: "24px auto",
                    boxShadow: "0 8px 32px rgba(0,0,0,0.4)",
                  },
                },
              }] : [{
                type: "div",
                props: {
                  style: {
                    width: 300, height: 300, borderRadius: "50%",
                    border: "5px dashed rgba(255,255,255,0.2)", margin: "24px auto",
                    display: "flex", alignItems: "center", justifyContent: "center",
                    fontSize: 64, background: "rgba(255,255,255,0.03)",
                  },
                  children: ["\u{1F43E}"],
                },
              }]),
              // Punchline
              ...(punchline ? [{
                type: "div",
                props: {
                  style: { fontSize: 24, lineHeight: 1.5, color: "rgba(255,255,255,0.85)", marginTop: 24, whiteSpace: "pre-line", display: "flex" },
                  children: [punchline],
                },
              }] : []),
            ],
          },
        },
        // Brand mark
        {
          type: "div",
          props: {
            style: {
              position: "absolute", bottom: 24, right: 32,
              fontSize: 11, color: "rgba(255,255,255,0.25)",
              letterSpacing: 3, textTransform: "uppercase", fontWeight: 600, zIndex: 1,
              display: "flex",
            },
            children: ["ROAST.PET"],
          },
        },
      ],
    },
  };

  // Render with Satori
  const svg = await satori(jsx, {
    width: CARD.w,
    height: CARD.h,
    fonts: [
      ...(fontData ? [{ name: "Inter", data: fontData, weight: 400 }] : []),
      ...(fontBoldData ? [{ name: "Inter", data: fontBoldData, weight: 700 }] : []),
      ...(fontBlackData ? [{ name: "Inter", data: fontBlackData, weight: 900 }] : []),
    ],
  });

  // Render SVG → PNG with resvg
  const resvg = new Resvg(svg, {
    fitTo: { mode: "width", value: CARD.w },
    font: { loadSystemFonts: true },
  });
  const pngData = resvg.render();
  return Buffer.from(pngData.asPng());
}

/**
 * Composite pet photo onto a card template
 * Crops pet photo to circle and composites onto card
 */
export async function compositePetPhoto(cardPng, petPhotoBuffer) {
  if (!petPhotoBuffer) return cardPng;

  const circleSize = 300;
  const circleSvg = `<svg width="${circleSize}" height="${circleSize}">
    <circle cx="${circleSize/2}" cy="${circleSize/2}" r="${circleSize/2}" fill="white"/>
  </svg>`;

  const circleMask = Buffer.from(circleSvg);
  const resizedPet = await sharp(petPhotoBuffer)
    .resize(circleSize, circleSize, { fit: "cover" })
    .composite([{ input: circleMask, blend: "dest-in" }])
    .png()
    .toBuffer();

  // Position: centered horizontally, ~40% from top
  const x = Math.round((CARD.w - circleSize) / 2);
  const y = Math.round(CARD.h * 0.35);

  return sharp(cardPng)
    .composite([{ input: resizedPet, left: x, top: y }])
    .png({ quality: 100 })
    .toBuffer();
}

/**
 * Render full card with pet photo composited
 */
export async function renderFullCard({ setup, punchline, petPhotoBuffer, roast }) {
  const cardPng = await renderCard({ setup, punchline, roast, side: "front" });
  return await compositePetPhoto(cardPng, petPhotoBuffer);
}

// CLI usage
if (process.argv[1] && process.argv[1].includes("render-card")) {
  const args = JSON.parse(process.argv[2] || "{}");
  const petBuf = args.pet_photo ? readFileSync(args.pet_photo) : null;
  const outPath = args.output || "/tmp/card-print.png";

  const png = await renderFullCard({
    setup: args.setup || "Your Headline",
    punchline: args.punchline || "Your punchline here",
    petPhotoBuffer: petBuf,
    roast: args.roast || "roast",
  });

  const { writeFileSync } = await import("fs");
  writeFileSync(outPath, png);
  console.log(JSON.stringify({ file: outPath, size: png.length, dimensions: { w: CARD.w, h: CARD.h } }));
}
