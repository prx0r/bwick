/**
 * Prodigi API integration for card printing
 * REST v4 API — sandbox mode (no real charges)
 */
const PRODIGI_BASE = "https://sandbox-api.prodigi.com/v4.0";
const API_KEY = process.env.PRODIGI_API_KEY || "";

/**
 * Get product catalog / pricing
 */
export async function getProduct(sku = "card_a5_350gsm") {
  if (!API_KEY) return { sandbox: true, sku, unit_cost: 3.50, currency: "GBP" };
  const resp = await fetch(`${PRODIGI_BASE}/products/${sku}`, {
    headers: { "Authorization": `Bearer ${API_KEY}` }
  });
  return resp.json();
}

/**
 * Create a print order
 * @param {Object} opts
 * @param {string} opts.imageUrl - URL of the card image (hosted or base64 data URI)
 * @param {Object} opts.shippingAddress
 * @param {string} opts.recipientName
 */
export async function createOrder({ imageUrl, shippingAddress, recipientName }) {
  if (!API_KEY) {
    return {
      sandbox: true,
      order_id: "sandbox_" + Date.now(),
      status: "pending",
      message: "Sandbox mode — wire PRODIGI_API_KEY for real orders"
    };
  }

  const payload = {
    merchantReference: "roast.pet_" + Date.now(),
    shippingMethod: "standard",
    recipientEmail: shippingAddress.email || "",
    items: [
      {
        sku: "card_a5_350gsm",
        copies: 1,
        recipientCost: { amount: 6.49, currency: "GBP" },
        assets: [
          {
            url: imageUrl,
            printArea: "front",
          },
        ],
      },
    ],
    shippingAddress: {
      firstName: recipientName || shippingAddress.name || "",
      lastName: "",
      address1: shippingAddress.line1 || "",
      address2: shippingAddress.line2 || "",
      city: shippingAddress.city || "",
      stateOrProvince: shippingAddress.state || "",
      postalCode: shippingAddress.postcode || "",
      country: shippingAddress.country || "GB",
      phone: shippingAddress.phone || "",
    },
  };

  const resp = await fetch(`${PRODIGI_BASE}/orders`, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  return resp.json();
}

/**
 * Get order status
 */
export async function getOrder(orderId) {
  if (!API_KEY) return { order_id: orderId, status: "sandbox_pending" };
  const resp = await fetch(`${PRODIGI_BASE}/orders/${orderId}`, {
    headers: { "Authorization": `Bearer ${API_KEY}` }
  });
  return resp.json();
}

/**
 * Quote an order (get price without placing it)
 */
export async function quoteOrder(sku = "card_a5_350gsm", destination = "GB") {
  if (!API_KEY) {
    return {
      sandbox: true,
      items: [{ sku, unit_cost: 3.50, currency: "GBP" }],
      shipping: { method: "standard", cost: 2.99, currency: "GBP", estimated_days: 5 },
      total: 6.49,
    };
  }
  const resp = await fetch(`${PRODIGI_BASE}/orders/quote`, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      items: [{ sku, copies: 1 }],
      destination: { country: destination },
    }),
  });
  return resp.json();
}
