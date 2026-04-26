module.exports = function(eleventyConfig) {
  // Passthrough copy for assets
  eleventyConfig.addPassthroughCopy("src/assets");
  
  // Watch for asset changes
  eleventyConfig.addWatchTarget("src/assets");
  
  // Ghazals collection
  eleventyConfig.addCollection("ghazals", function(collectionApi) {
    return collectionApi.getFilteredByGlob("src/content/ghazals/*.json");
  });
  
  // Nazms collection
  eleventyConfig.addCollection("nazms", function(collectionApi) {
    return collectionApi.getFilteredByGlob("src/content/nazms/*.json");
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