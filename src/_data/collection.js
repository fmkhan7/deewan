module.exports = {
  eleventyComputed: {
    collection: (data) => {
      const collections = data.poetry_collections || [];
      const activeSlug = data.site.activeCollection || 'deewan-e-ekta';
      return collections.find(c => c.slug === activeSlug) || collections[0] || {};
    }
  }
};