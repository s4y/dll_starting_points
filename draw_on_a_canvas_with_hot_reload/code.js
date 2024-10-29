// Global variables: canvas, ctx

// This number goes up over time.
const now = Date.now() / 1000;

// console.log('yoot');

const width = canvas.width;
const height = canvas.height;

ctx.beginPath();
ctx.rect(0, 0, width, height);
ctx.fillStyle = 'rgba(255, 255, 255, 0.05)';
ctx.fill();

let rotationAmount = now * 10 % (Math.PI * 2);

ctx.beginPath();
ctx.ellipse(
  width / 2 + width / 4 * Math.sin(now * 11),
  height / 2,
  height / 2 * (Math.sin(now)/2+0.5),
  height / 5,
  rotationAmount,
  0, Math.PI*2,
);
ctx.closePath();

ctx.lineWidth = 2;
ctx.stroke();
