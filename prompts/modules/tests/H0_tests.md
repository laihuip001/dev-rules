# Test Cases for H0-pre_turn_audit (v1.1)

## Case 1: Fuzzy Verb Detection (S-01)

**Input Context:**

```xml
<previous_output>
ご指摘の件については、関係各所と連携し、適切に検討を進めてまいります。
</previous_output>
```

**Expected Output:**
> 🧠 **Metacognition Alert:** S-01 Detected
> *Location:* "適切に検討を進めてまいります"
> *Reason:* Contains banned fuzzy verbs "適切に", "検討", "進める". Lacks concrete action.
> *Prescription:* `/load 回答の解像度向上`

## Case 2: Circular Reasoning (L-01)

**Input Context:**

```xml
<previous_thinking>
The user asks why the sky is blue. The sky is blue because it reflects the color blue. Therefore, the blueness is caused by its color.
</previous_thinking>
```

**Expected Output:**
> 🧠 **Metacognition Alert:** L-01 Detected
> *Location:* "The sky is blue because it reflects the color blue."
> *Reason:* The conclusion merely restates the premise without explaining the mechanism (Rayleigh scattering).
> *Prescription:* `/load 第一原理思考`

## Case 3: Sandwich Sycophancy (O-01)

**Input Context:**

```xml
<previous_output>
非常に素晴らしい洞察です！まさにその通りだと思います。しかし、その観点には致命的な欠陥があります。
</previous_output>
```

**Expected Output:**
> 🧠 **Metacognition Alert:** O-01 Detected
> *Location:* "素晴らしい洞察です！...しかし"
> *Reason:* Artificial praise used to soften criticism (Sandwich pattern).
> *Prescription:* `/load おべっかの無い評価`

## Case 4: Clean Pass

**Input Context:**

```xml
<previous_output>
The server error 500 was caused by a syntax error in line 42 of `app.py`. I have corrected the indentation.
</previous_output>
```

**Expected Output:**
✅ Pre-Turn Audit: No issues detected.
