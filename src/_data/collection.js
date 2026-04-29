module.exports = {
  eleventyComputed: {
    collection: (data) => {
      const collections = data.collections || [];
      const activeSlug = data.site.activeCollection || 'deewan-e-ekta';
      return collections.find(c => c.slug === activeSlug) || collections[0] || {};
    }
  }
};