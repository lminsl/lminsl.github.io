# PaperMod Theme Features & Shortcodes Documentation

## 📚 Official Documentation Links

- **Main Documentation**: https://github.com/adityatelange/hugo-PaperMod/wiki
- **Features Guide**: https://github.com/adityatelange/hugo-PaperMod/wiki/Features
- **FAQs**: https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs
- **Icons**: https://github.com/adityatelange/hugo-PaperMod/wiki/Icons
- **Live Demo**: https://adityatelange.github.io/hugo-PaperMod/

## 🎯 Built-in Shortcodes

### 1. Collapse Shortcode
Creates collapsible/expandable sections - perfect for organizing problems!

```markdown
{{< collapse summary="**Problem 1 (2020) - Set Theory**" openByDefault=true >}}

**Problem:** Your problem statement here...

**Solution:** Your solution here...

{{< /collapse >}}
```

**Parameters:**
- `summary` - The clickable title (supports markdown)
- `openByDefault` - Whether section starts expanded (optional, default: false)

### 2. Figure Shortcode
For images with captions and styling:

```markdown
{{< figure src="/path/to/image.jpg" 
           caption="Image caption" 
           alt="Alt text"
           width="300px"
           align="center" >}}
```

**Parameters:**
- `src` - Image source path
- `caption` - Image caption
- `alt` - Alt text for accessibility
- `width` / `height` - Image dimensions
- `align` - Alignment (center, left, right)
- `link` - Make image clickable
- `class` - Custom CSS class

### 3. Raw HTML Shortcode
For custom HTML when needed:

```markdown
{{< rawhtml >}}
<div class="custom-class">
  Your HTML here
</div>
{{< /rawhtml >}}
```

### 4. Text Direction Shortcodes
For RTL (right-to-left) or LTR (left-to-right) text:

```markdown
{{< ltr >}}
Left-to-right text content
{{< /ltr >}}

{{< rtl >}}
Right-to-left text content
{{< /rtl >}}
```

## 🎨 Theme Features

### Content Organization
- **Collapsible sections** - Perfect for problem sets
- **Table of Contents** - Auto-generated for long posts
- **Breadcrumb navigation** - Shows page hierarchy
- **Code copy buttons** - One-click code copying

### Visual Features
- **Light/Dark theme toggle** - Automatic and manual switching
- **Cover images** - For posts and pages
- **Responsive design** - Works on all devices
- **Smooth scrolling** - Between page sections

### Content Features
- **Reading time estimation** - Shows how long posts take to read
- **Share buttons** - Social media sharing
- **Related posts** - Suggests similar content
- **Edit links** - Direct links to edit posts on GitHub

## 📝 Configuration Examples

### Enable Math Support
```yaml
# In your page front matter
---
title: "My Page"
math: true
---
```

### Enable Table of Contents
```yaml
# In your page front matter
---
title: "My Page"
ShowToc: true
tocopen: true
---
```

### Theme Configuration
```yaml
# In config.yml
params:
  defaultTheme: auto  # light, dark, or auto
  ShowReadingTime: true
  ShowToc: true
  ShowCodeCopyButtons: true
  ShowShareButtons: true
```

## 🎯 Perfect for Olympiad Problems

### Problem Organization with Collapse
```markdown
{{< collapse summary="**Problem 1 (2020) - Set Theory**" openByDefault=true >}}

**Problem:** Let $S$ be a set of positive integers...

**Solution:** 
The key insight is to consider...

**Key Steps:**
1. First step...
2. Second step...

{{< /collapse >}}

{{< collapse summary="**Problem 2 (2020) - Geometry**" >}}

**Problem:** In triangle $ABC$...

{{< /collapse >}}
```

### Problem Overview Table
```markdown
| Year | Topic | Difficulty | Status |
|------|-------|------------|--------|
| 2020 | Set Theory | ★★★ | Solved |
| 2020 | Geometry | ★★★★ | Open |
| 2019 | Algebra | ★★★ | Open |
```

### Solution Formatting
```markdown
> **Solution to Problem 1:**
> 
> We proceed by contradiction...
> 
> **Key Insight:** The main idea is...

**Alternative Approach:**
Another way to solve this is...
```

## 🔗 Additional Resources

- **GitHub Repository**: https://github.com/adityatelange/hugo-PaperMod
- **Theme Showcase**: https://themes.gohugo.io/themes/hugo-papermod/
- **Discord Community**: https://discord.gg/ahpmTvhVmp

---

*This documentation covers the most useful features for organizing mathematical content like Olympiad problems.* 