export const weights: Record<string, number> = {
  credential_request: 45, pressure: 30, payment: 40,
  unencrypted_http: 25, userinfo_in_url: 45,
  internationalized_domain: 15, ip_address_host: 20
};
export type Assessment = { score: number | null; risk: string; signals: string[] };
export function scoreSignals(signals: string[]): Assessment {
  const unique = [...new Set(signals)].sort();
  const score = Math.min(100, unique.reduce((n, s) => n + (weights[s] ?? 0), 0));
  return { score, risk: score >= 60 ? "high" : score > 0 ? "caution" : "unknown", signals: unique };
}
export function analyzeText(text: string): Assessment {
  if (text.length > 10000) throw new Error("Input too long");
  const normalized = text.toLowerCase().replace(/\s+/g, " ");
  const rules: Record<string, string[]> = {
    credential_request: ["verify your password", "send your password", "share your otp", "enter your one time password"],
    pressure: ["act immediately", "account will be suspended", "urgent action required"],
    payment: ["pay a verification fee", "send gift cards"]
  };
  return scoreSignals(Object.entries(rules).filter(([, phrases]) => phrases.some(p => normalized.includes(p))).map(([key]) => key));
}
export function analyzeUrl(input: string): Assessment {
  if (input.length > 10000) throw new Error("Input too long");
  try {
    const url = new URL(input.trim());
    if (!["http:", "https:"].includes(url.protocol) || !url.hostname) throw new Error("Invalid URL");
    const signals: string[] = [];
    if (url.protocol === "http:") signals.push("unencrypted_http");
    if (/^https?:\/\/[^/]*@/.test(input.trim())) signals.push("userinfo_in_url");
    if (url.hostname.startsWith("xn--") || url.hostname.includes(".xn--")) signals.push("internationalized_domain");
    if (/^\d{1,3}(\.\d{1,3}){3}$/.test(url.hostname)) signals.push("ip_address_host");
    return scoreSignals(signals);
  } catch { return { score: null, risk: "invalid", signals: ["invalid_url"] }; }
}
