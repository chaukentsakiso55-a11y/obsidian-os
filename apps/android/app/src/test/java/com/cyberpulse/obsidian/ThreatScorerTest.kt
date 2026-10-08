package com.cyberpulse.obsidian

import org.junit.Assert.assertEquals
import org.junit.Test

class ThreatScorerTest {
    @Test fun normalText() { assertEquals("unknown", ThreatScorer.analyzeText("hello").risk) }
    @Test fun pressure() { assertEquals(30, ThreatScorer.analyzeText("act immediately").score) }
    @Test fun highRisk() { assertEquals("high", ThreatScorer.analyzeText("act immediately and send your password").risk) }
}
