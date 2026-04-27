module.exports = function(eleventyConfig) {
  // Passthrough copy for assets
  eleventyConfig.addPassthroughCopy("src/assets");
  
  // Watch for asset changes
  eleventyConfig.addWatchTarget("src/assets");
  
  const fs = require('fs');
  const path = require('path');
  
  // Custom filter to read ghazals JSON directly
  eleventyConfig.addFilter("ghazals", function() {
    const ghazalsDir = path.join(__dirname, 'src/content/ghazals');
    const files = fs.readdirSync(ghazalsDir).filter(f => f.endsWith('.json'));
    return files.map(f => {
      const data = JSON.parse(fs.readFileSync(path.join(ghazalsDir, f), 'utf8'));
      return { data: data };
    });
  });
  
  // Custom filter to read nazms JSON directly
  eleventyConfig.addFilter("nazms", function() {
    const nazmsDir = path.join(__dirname, 'src/content/nazms');
    const files = fs.readdirSync(nazmsDir).filter(f => f.endsWith('.json'));
    return files.map(f => {
      const data = JSON.parse(fs.readFileSync(path.join(nazmsDir, f), 'utf8'));
      return { data: data };
    });
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