const canvas = document.getElementById('pongCanvas');
const ctx = canvas.getContext('2d');

// Game variables
const paddleWidth = 12, paddleHeight = 90;
const ballRadius = 10;
const playerX = 20;
const aiX = canvas.width - paddleWidth - 20;
let playerY = (canvas.height - paddleHeight) / 2;
let aiY = (canvas.height - paddleHeight) / 2;
let playerScore = 0, aiScore = 0;

// Ball state
let ball = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    vx: 6 * (Math.random() < 0.5 ? 1 : -1),
    vy: (Math.random() - 0.5) * 8
};

function resetBall() {
    ball.x = canvas.width / 2;
    ball.y = canvas.height / 2;
    ball.vx = 6 * (Math.random() < 0.5 ? 1 : -1);
    ball.vy = (Math.random() - 0.5) * 8;
}

function drawRect(x, y, w, h, color="#fff") {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, w, h);
}

function drawCircle(x, y, r, color="#fff") {
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.fillStyle = color;
    ctx.fill();
}

function drawNet() {
    for (let i = 0; i < canvas.height; i += 25) {
        drawRect(canvas.width / 2 - 2, i, 4, 15, "#666");
    }
}

function drawScore() {
    ctx.font = "32px Arial";
    ctx.fillStyle = "#fff";
    ctx.fillText(playerScore, canvas.width / 4, 40);
    ctx.fillText(aiScore, 3 * canvas.width / 4, 40);
}

// Mouse control for player paddle
canvas.addEventListener('mousemove', function(evt) {
    const rect = canvas.getBoundingClientRect();
    let mouseY = evt.clientY - rect.top;
    playerY = mouseY - paddleHeight / 2;
    // Clamp within bounds
    if (playerY < 0) playerY = 0;
    if (playerY > canvas.height - paddleHeight) playerY = canvas.height - paddleHeight;
});

// Simple AI for right paddle
function aiMove() {
    let center = aiY + paddleHeight / 2;
    if (center < ball.y - 10)
        aiY += 5;
    else if (center > ball.y + 10)
        aiY -= 5;

    // Clamp to bounds
    if (aiY < 0) aiY = 0;
    if (aiY > canvas.height - paddleHeight) aiY = canvas.height - paddleHeight;
}

// Collision detection
function collision(px, py) {
    // px, py: paddle x, y
    return (
        ball.x + ballRadius > px &&
        ball.x - ballRadius < px + paddleWidth &&
        ball.y + ballRadius > py &&
        ball.y - ballRadius < py + paddleHeight
    );
}

// Main update loop
function update() {
    // Move ball
    ball.x += ball.vx;
    ball.y += ball.vy;

    // Wall collisions (top/bottom)
    if (ball.y - ballRadius < 0 || ball.y + ballRadius > canvas.height) {
        ball.vy = -ball.vy;
        // Clamp inside
        if (ball.y - ballRadius < 0) ball.y = ballRadius;
        if (ball.y + ballRadius > canvas.height) ball.y = canvas.height - ballRadius;
    }

    // Paddle collisions
    // Player paddle
    if (ball.vx < 0 && collision(playerX, playerY)) {
        ball.vx = -ball.vx * 1.05;
        // Add some "spin"
        ball.vy += ((ball.y - (playerY + paddleHeight / 2)) / (paddleHeight / 2)) * 4;
        ball.x = playerX + paddleWidth + ballRadius; // prevent sticking
    }
    // AI paddle
    else if (ball.vx > 0 && collision(aiX, aiY)) {
        ball.vx = -ball.vx * 1.05;
        // Add some "spin"
        ball.vy += ((ball.y - (aiY + paddleHeight / 2)) / (paddleHeight / 2)) * 4;
        ball.x = aiX - ballRadius; // prevent sticking
    }

    // Score check
    if (ball.x - ballRadius < 0) {
        aiScore++;
        resetBall();
    }
    if (ball.x + ballRadius > canvas.width) {
        playerScore++;
        resetBall();
    }

    aiMove();
}

// Main draw function
function draw() {
    // Clear
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawNet();
    drawScore();

    // Draw paddles
    drawRect(playerX, playerY, paddleWidth, paddleHeight);
    drawRect(aiX, aiY, paddleWidth, paddleHeight);

    // Draw ball
    drawCircle(ball.x, ball.y, ballRadius);
}

// Game loop
function loop() {
    update();
    draw();
    requestAnimationFrame(loop);
}

loop();