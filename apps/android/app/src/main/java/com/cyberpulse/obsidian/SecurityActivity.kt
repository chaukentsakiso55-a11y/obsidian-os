package com.cyberpulse.obsidian

import android.app.Activity
import android.os.Bundle
import android.graphics.Color
import android.view.ViewGroup
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.ScrollView
import android.widget.TextView

class SecurityActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val layout = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(28, 45, 28, 28)
            setBackgroundColor(Color.rgb(7, 12, 21))
        }
        fun text(value: String, size: Float): TextView = TextView(this).apply {
            this.text = value
            textSize = size
            setTextColor(Color.rgb(190, 220, 245))
            setPadding(0, 12, 0, 12)
        }
        layout.addView(text("◈ OBSIDIAN", 29f))
        layout.addView(text("LOCAL SECURITY GUARDIAN · PROTOTYPE", 12f))
        layout.addView(text("Analyze suspicious messages offline. No data is transmitted.", 17f))
        val input = EditText(this).apply {
            hint = "Paste a suspicious message"
            setHintTextColor(Color.LTGRAY)
            setTextColor(Color.WHITE)
            minLines = 4
            maxLines = 8
            inputType = android.text.InputType.TYPE_CLASS_TEXT or android.text.InputType.TYPE_TEXT_FLAG_MULTI_LINE
        }
        layout.addView(input, LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT))
        val result = text("Ready for local analysis", 18f)
        val button = Button(this).apply {
            text = "Analyze message"
            setOnClickListener {
                val value = input.text.toString()
                if (value.isBlank()) result.text = "Enter a message first."
                else try {
                    val assessment = ThreatScorer.analyzeText(value)
                    result.text = "Risk: ${assessment.risk.uppercase()}\nScore: ${assessment.score}/100\nSignals: ${assessment.signals.joinToString().ifBlank { "None detected" }}\n\nLow scores do not guarantee safety."
                } catch (e: IllegalArgumentException) { result.text = e.message }
            }
        }
        layout.addView(button)
        layout.addView(result)
        val scroll = ScrollView(this)
        scroll.addView(layout)
        setContentView(scroll)
    }
}
