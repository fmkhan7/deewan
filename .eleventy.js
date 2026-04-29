module.exports = function(eleventyConfig) {
  // Passthrough copy for assets
  eleventyConfig.addPassthroughCopy("src/assets");
  
  // Watch for asset changes
  eleventyConfig.addWatchTarget("src/assets");
  
  const fs = require('fs');
  const path = require('path');
  
  // Poetry collections data
  const poetry_collections = [
    {
      slug: "deewan-e-ekta",
      title: "دیوان یکتا",
      titleEn: "Deewan-e-Ekta",
      author: "یکتا",
      authorEn: "Ekta",
      description: "Urdu Poetry Collection",
      language: "ur",
      default: true
    },
    {
      slug: "deewan-ghalib",
      title: "دیوان غالب",
      titleEn: "Deewan-e-Ghalib",
      author: "غالب",
      authorEn: "Ghalib",
      description: "Another Urdu Poetry Collection",
      language: "ur",
      default: false
    }
  ];
  
  // Add collections to global data
  eleventyConfig.addGlobalData("poetry_collections", poetry_collections);
  
  // Add data to global data cascade
  eleventyConfig.addGlobalData("ghazals", function() {
    try {
      const ghazalsDir = path.join(__dirname, 'src/content/ghazals');
      const files = fs.readdirSync(ghazalsDir).filter(f => f.endsWith('.json'));
      return files.map(f => {
        const data = JSON.parse(fs.readFileSync(path.join(ghazalsDir, f), 'utf8'));
        return { data: data };
      });
    } catch (e) {
      console.error('Error loading ghazals:', e);
      return [];
    }
  });
  
  // Add data to global data cascade
  eleventyConfig.addGlobalData("nazms", function() {
    try {
      const nazmsDir = path.join(__dirname, 'src/content/nazms');
      if (!fs.existsSync(nazmsDir)) return [];
      const files = fs.readdirSync(nazmsDir).filter(f => f.endsWith('.json'));
      return files.map(f => {
        const data = JSON.parse(fs.readFileSync(path.join(nazmsDir, f), 'utf8'));
        return { data: data };
      });
    } catch (e) {
      console.error('Error loading nazms:', e);
      return [];
    }
  });
  
  // Urdu date filter
  eleventyConfig.addFilter("urduDate", (date) => {
    if (!date) return "";
    const urduNumerals = ['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹'];
    const year = date.getFullYear().toString().split('').map(d => urduNumerals[parseInt(d)]).join('');
    const month = (date.getMonth() + 1).toString().split('').map(d => urduNumerals[parseInt(d)]).join('');
    const day = date.getDate().toString().split('').map(d => urduNumerals[parseInt(d)]).join('');
    return `${day}/${month}/${year}`;
  });
  
  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data"
    },
    templateFormats: ["md", "njk", "html", "liquid", "json"],
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk"
  };
};