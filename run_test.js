const { execSync } = require('child_process');

try {
  const output = execSync('node test_clean_web_static.js', { encoding: 'utf-8' });
  console.log(output);
} catch (error) {
  console.error('Error running tests:', error.message);
}