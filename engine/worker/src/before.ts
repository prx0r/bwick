import { templates, selectTemplate } from "./templates";
import { generateJokes } from "./jokes";

interface Env { ASSETS: Fetcher; }

const S: Record<string,[string,string,string]> = {
  thought_bubble: ["Owner: Will AGI replace me?","Dog: Will dinner still be at six?","#4ec9b0"],
  pet_standup: ["So my owner calls themselves a pet parent","You forgot to feed me on Tuesday. I counted.","#ff6b6b"],
  breaking_news: ["BREAKING: Local Man Spotted","Doing Something Competent. Witnesses Shocked.","#569cd6"],
  performance_review: ["ANNUAL PERFORMANCE REVIEW","Food Delivery: Inconsistent. Walks: Cancelled 3x.","#dcdcaa"],
  pet_therapist: ["Session Notes:","Owner exhibits one more episode syndrome. Terminal.","#4ec9b0"],
  search_history: ["RECENT SEARCHES:","how to report owner for late dinner","#c586c0"],
  complaint_dept: ["FORMAL COMPLAINT","Subject: Chronic late-feeding. Excessive phone usage.","#f44747"],
  split_panel: ["Human: Will AGI take my job?","Dog: Will the squirrel come back tomorrow?","#569cd6"],
  incident_report: ["INCIDENT REPORT #0032","Subject completed another year. Decline noted.","#ce9178"],
  wildcard: ["We saw your pet and had questions.","Here are the answers you didn't know you needed.","#ff8844"],
  xmas_santa_automated: ["Merry Christmas!","Your role has been automated.","#ff6b6b"],
  xmas_santa_vs_robots: ["BREAKING:","10 million robots disabled in sleigh attack.","#569cd6"],
  xmas_elf_redundancy: ["MEMO: North Pole Restructuring","47 elf positions eliminated after agent deployment.","#dcdcaa"],
  xmas_pet_security: ["SECURITY REPORT:","STRANGER ENTERED VIA CHIMNEY. DOG ACCEPTED BISCUIT.","#f44747"],
  xmas_performance_review: ["CHRISTMAS REVIEW","Turkey: adequate. Walks: unacceptable. Wrapping: embarrassing.","#ce9178"],
  xmas_human_vs_pet: ["Human: Will Christmas feel human after AGI?","Dog: Turkey.","#4ec9b0"],
  xmas_cat_vs_tree: ["INCIDENT REPORT","Decorative structure destroyed 14 min after deployment.","#f44747"],
  xmas_santa_search_history: ["Santa reads your search history:","is santa edible / reindeer territorial rights","#c586c0"],
  xmas_ai_card: ["Human: Will Christmas feel human after AGI?","Dog: You bought this card from an AI.","#ff6b6b"],
  xmas_pet_complaint: ["FORMAL COMPLAINT TO SANTA","Requesting replacement owner. Current unit misses feeding windows.","#dcdcaa"],
};


function cardSvg(setup: string, punchline: string, petUrl: string, roast: string, template?: string) {
  const s = S[template || ""] || S.thought_bubble;
  const headline = setup || s[0];
  const punch = punchline || s[1];
  const cardColor = s[2];
  const petEl = petUrl
    ? '<image href="'+petUrl+'" x="374" y="880" width="300" height="300" clip-path="circle(150px at 150px 150px)" />'
    : '<circle cx="524" cy="1030" r="150" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="5" stroke-dasharray="10 5" /><text x="524" y="1038" text-anchor="middle" fill="rgba(255,255,255,0.3)" font-size="48">&#x1F43E;</text>';

  const wrap = (t: string, max: number) => {
    const words = t.split(" "); const lines: string[] = []; let line = "";
    for (const w of words) { if ((line+" "+w).length > max && line) { lines.push(line); line = w; } else line = line ? line+" "+w : w; }
    if (line) lines.push(line); return lines;
  };

  const hLines = wrap(headline, 28);
  const pLines = wrap(punch, 32);
  const hY = petUrl ? 380 : 580;
  const hSvg = hLines.map((l,i) => '<text x="524" y="'+(hY+i*55)+'" text-anchor="middle" fill="white" font-size="42" font-weight="900" font-family="system-ui,sans-serif">'+esc(l)+'</text>').join("\n");
  const pY = petUrl ? 1250 : 1300;
  const pSvg = pLines.map((l,i) => '<text x="524" y="'+(pY+i*36)+'" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="24" font-family="system-ui,sans-serif">'+esc(l)+'</text>').join("\n");

  return '<svg xmlns="http://www.w3.org/2000/svg" width="1050" height="1470" viewBox="0 0 1050 1470">'
    + '<defs><radialGradient id="g1" cx="30%" cy="70%"><stop offset="0%" stop-color="'+cardColor+'22"/><stop offset="100%" stop-color="transparent"/></radialGradient>'
    + '<radialGradient id="g2" cx="70%" cy="30%"><stop offset="0%" stop-color="'+cardColor+'11"/><stop offset="100%" stop-color="transparent"/></radialGradient></defs>'
    + '<rect width="1050" height="1470" fill="#1a1a2e"/>'
    + '<rect width="1050" height="1470" fill="url(#g1)"/>'
    + '<rect width="1050" height="1470" fill="url(#g2)"/>'
    + '<rect x="24" y="24" width="80" height="32" rx="16" fill="'+cardColor+'22"/>'
    + '<text x="36" y="46" fill="'+cardColor+'" font-size="11" font-weight="700" font-family="system-ui" letter-spacing="1.5">'+roast.toUpperCase()+'</text>'
    + hSvg + petEl + pSvg
    + '<text x="1020" y="1446" text-anchor="end" fill="rgba(255,255,255,0.25)" font-size="11" font-weight="600" font-family="system-ui" letter-spacing="3">ROAST.PET</text>'
    + '</svg>';
}

function esc(s: string) { return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;"); }

