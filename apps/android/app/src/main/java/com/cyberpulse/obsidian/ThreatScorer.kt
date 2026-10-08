package com.cyberpulse.obsidian

data class Assessment(val score: Int, val risk: String, val signals: List<String>)

object ThreatScorer {
    private val weights = mapOf("credential_request" to 45, "pressure" to 30, "payment" to 40)
    private val phrases = mapOf(
        "credential_request" to listOf("verify your password", "send your password", "share your otp", "enter your one time password"),
        "pressure" to listOf("act immediately", "account will be suspended", "urgent action required"),
        "payment" to listOf("pay a verification fee", "send gift cards")
    )
    fun analyzeText(text: String): Assessment {
        require(text.length <= 10000) { "Input too long" }
        val normalized = text.lowercase().replace(Regex("\\s+"), " ")
        val signals = phrases.filter { (_, values) -> values.any { normalized.contains(it) } }.keys.sorted()
        val score = signals.sumOf { weights[it] ?: 0 }.coerceAtMost(100)
        return Assessment(score, if (score >= 60) "high" else if (score > 0) "caution" else "unknown", signals)
    }
}
