# Color Text in Hugo - Complete Guide

## 🎨 Method 1: Raw HTML Shortcode (Most Flexible)

```markdown
{{< rawhtml >}}
<span style="color: #e74c3c; font-weight: bold;">🔴 Red text</span>
{{< /rawhtml >}}
```

## 🎨 Method 2: Inline HTML (Simpler)

```markdown
<span style="color: #3498db;">🔵 Blue text</span>
```

## 🎨 Method 3: CSS Classes (Most Professional)

After adding the custom CSS file, you can use these classes:

### Problem Types
```markdown
<span class="problem-important">🔴 Important Problem</span>
<span class="problem-geometry">🔵 Geometry Problem</span>
<span class="problem-solved">🟢 Solved Problem</span>
<span class="problem-challenging">🟡 Challenging Problem</span>
<span class="problem-number-theory">🟣 Number Theory Problem</span>
<span class="problem-algebra">🟠 Algebra Problem</span>
<span class="problem-combinatorics">🟣 Combinatorics Problem</span>
```

### Difficulty Levels
```markdown
<span class="difficulty-easy">Easy</span>
<span class="difficulty-medium">Medium</span>
<span class="difficulty-hard">Hard</span>
```

### Topic Tags
```markdown
<span class="topic-tag topic-set-theory">Set Theory</span>
<span class="topic-tag topic-geometry">Geometry</span>
<span class="topic-tag topic-algebra">Algebra</span>
<span class="topic-tag topic-number-theory">Number Theory</span>
<span class="topic-tag topic-combinatorics">Combinatorics</span>
```

### Problem Boxes
```markdown
{{< rawhtml >}}
<div class="problem-box problem-box-important">
  <strong>Problem 1:</strong> Your problem statement here...
</div>
{{< /rawhtml >}}
```

## 🎨 Method 4: Using Emojis for Visual Color

```markdown
🔴 **Important:** This is a key problem
🔵 **Geometry:** Triangle problem
🟢 **Solved:** This has a solution
🟡 **Challenging:** Very difficult
🟣 **Number Theory:** Prime numbers
🟠 **Algebra:** Polynomials
```

## 🎨 Method 5: LaTeX with Color (Advanced)

```markdown
{{< rawhtml >}}
<span style="color: #e74c3c;">$\color{red}{f(x) = x^2}$</span>
{{< /rawhtml >}}
```

## 🎨 Method 6: Custom Shortcode (Most Elegant)

Create a custom shortcode for colors:

```html
<!-- layouts/shortcodes/color.html -->
<span style="color: {{ .Get "color" }}; {{ with .Get "weight" }}font-weight: {{ . }};{{ end }}">{{ .Inner }}</span>
```

Then use it like:
```markdown
{{< color color="#e74c3c" weight="bold" >}}Red bold text{{< /color >}}
```

## 🎨 Color Palette for Math Problems

### Primary Colors
- **Red (#e74c3c)**: Important/Critical problems
- **Blue (#3498db)**: Geometry problems
- **Green (#27ae60)**: Solved problems
- **Orange (#f39c12)**: Challenging problems
- **Purple (#9b59b6)**: Number theory problems

### Secondary Colors
- **Dark Orange (#e67e22)**: Algebra problems
- **Dark Purple (#8e44ad)**: Combinatorics problems
- **Gray (#95a5a6)**: General text

## 🎨 Complete Example for Your Olympiad Page

```markdown
## Problems with Color Coding

{{< rawhtml >}}
<h3 class="problem-important">🔴 Problem 1 (2020) - Set Theory & Functions</h3>
{{< /rawhtml >}}

<span class="topic-tag topic-set-theory">Set Theory</span>
<span class="difficulty-hard">Hard</span>

**Problem:** Suppose that there exists a nonempty set $X \subset \mathbb{R}$...

{{< rawhtml >}}
<div class="problem-box problem-box-important">
  <strong>Solution:</strong> The key insight is...
</div>
{{< /rawhtml >}}
```

## 🎨 Tips for Using Colors

1. **Be Consistent**: Use the same colors for the same types of content
2. **Don't Overuse**: Too many colors can be distracting
3. **Consider Accessibility**: Ensure good contrast ratios
4. **Use Meaningfully**: Colors should add value, not just decoration
5. **Test on Different Themes**: Colors should work in both light and dark modes

---

*Choose the method that works best for your workflow!* 