const fs = require('fs');
const path = require('path');

// Path to your JSON file
const jsonPath = path.join(__dirname, '../data/trade-with-suli.json');
const jsonData = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

// Function to generate image path from material name
function getImagePath(materialName) {
  // Convert to lowercase, replace spaces with hyphens, and remove special characters
  const baseName = materialName
    .toLowerCase()
    .replace(/tradewithsuli\.com/g, '')
    .replace(/[^a-z0-9\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-');
  
  return `image/tws/materials/${baseName}.jpg`;
}

// Update all materials with image paths
jsonData.modules.forEach(module => {
  if (module.materials && Array.isArray(module.materials)) {
    module.materials.forEach(material => {
      if (!material.image) {
        material.image = getImagePath(material.name);
      }
    });
  }
});

// Save the updated JSON back to the file
fs.writeFileSync(jsonPath, JSON.stringify(jsonData, null, 2));

console.log('All materials have been updated with image paths!');
