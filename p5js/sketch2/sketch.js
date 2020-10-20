var angle = 0.0;
function setup() {
createCanvas(500, 500);
background(0, 30, 50);
}
function draw() {
if(mouseIsPressed) {
translate(mouseX, mouseY);
rotate(angle);
rect(-15, -15, 30, 30);
fill(255, 50, 0);
angle += 0.1;
}}
