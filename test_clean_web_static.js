const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Helper function to create test archives
function createTestArchives(count, prefix = 'web_static_') {
  const testDir = path.join(__dirname, 'test_releases');
  if (!fs.existsSync(testDir)) {
    fs.mkdirSync(testDir);
  }
  
  for (let i = 0; i < count; i++) {
    const fileName = `${prefix}${Date.now() + i}.tgz`;
    fs.writeFileSync(path.join(testDir, fileName), 'test content');
  }
}

// Helper function to count archives
function countArchives(prefix = 'web_static_') {
  const testDir = path.join(__dirname, 'test_releases');
  return fs.readdirSync(testDir).filter(file => file.startsWith(prefix)).length;
}

// Test cases
function runTest(number, initialCount) {
  console.log(`Testing: number = ${number}, ${initialCount} archives`);
  createTestArchives(initialCount);
  
  try {
    execSync(`python3 100-clean_web_static.py ${number}`);
  } catch (error) {
    console.error('Error executing the script:', error.message);
  }
  
  const remainingCount = countArchives();
  const expectedCount = Math.min(number === 0 ? 1 : number, initialCount);
  
  console.log(`Remaining archives: ${remainingCount}`);
  console.log(`Expected remaining: ${expectedCount}`);
  console.log(remainingCount === expectedCount ? 'PASS' : 'FAIL');
  console.log('---');
}

// Run test cases
runTest(0, 1);  // number = 0, 1 archive
runTest(0, 2);  // number = 0, 2 archives
runTest(4, 5);  // number = 4, 5 archives
runTest(3, 5);  // number = 3, 5 archives
runTest(4, 2);  // number = 4, 2 archives

// Clean up test directory
fs.rmdirSync(path.join(__dirname, 'test_releases'), { recursive: true });