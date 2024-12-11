// Handle Drag and Drop
const uploadBox = document.getElementById('upload-box');
const gameImage = document.getElementById('game-image');
const predictedMove = document.getElementById('predicted-move');
const outputBox = document.getElementById('output-box');

// Add Drag and Drop Events
uploadBox.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadBox.style.borderColor = 'white';
});

uploadBox.addEventListener('dragleave', () => {
    uploadBox.style.borderColor = 'grey';
});

uploadBox.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadBox.style.borderColor = 'grey';
    const file = e.dataTransfer.files[0];
    if (file) {
        displayUploadedFile(file);
    }
});

// Add Change Event for File Input
gameImage.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        displayUploadedFile(file);
    }
});



// Display Uploaded File
function displayUploadedFile(file) {
    const reader = new FileReader();
    reader.onload = (e) => {
        uploadBox.style.backgroundImage = `url(${e.target.result})`;
        uploadBox.style.backgroundSize = 'cover';
        uploadBox.style.backgroundPosition = 'center';
    };
    reader.readAsDataURL(file);

    // Simulate Prediction after Upload
    simulatePrediction();
}

// Simulate Prediction (Replace with Actual AI Logic)
function simulatePrediction() {
    setTimeout(() => {
        outputBox.querySelector('p').style.display = 'none';
        predictedMove.src = 'path/to/sample-prediction-image.png'; // Replace with dynamic AI output
        predictedMove.style.display = 'block';
    }, 2000); // Simulate 2s delay
}

// async function startCamera() {
//     try {
//         const video = document.getElementById('video');
//         const initialText = document.getElementById('initialText');

//         const stream = await navigator.mediaDevices.getUserMedia({ video: true });
//         video.srcObject = stream;

//         // Remove initial text when video starts playing
//         video.addEventListener('playing', () => {
//             video.classList.add('playing');
//         });
//     } catch (error) {
//         console.error("Error accessing camera: ", error);
//         alert("Unable to access the camera. Please check your permissions.");
//     }
// }

let currentStream = null;
let useRearCamera = true; // Default to rear camera

async function startCamera() {
    // Stop any active stream
    if (currentStream) {
        currentStream.getTracks().forEach(track => track.stop());
    }

    try {
        const video = document.getElementById('video');
        const initialText = document.getElementById('initialText');
        const constraints = {
            video: {
                facingMode: useRearCamera ? "environment" : "user"
            }
        };

        currentStream = await navigator.mediaDevices.getUserMedia(constraints);
        video.srcObject = currentStream;

        // Remove initial text when video starts playing
        video.addEventListener('playing', () => {
            video.classList.add('playing');
        });
    } catch (error) {
        console.error("Error accessing camera: ", error);
        alert("Unable to access the camera. Please check your permissions.");
    }
}

// Start the camera when the page loads
window.addEventListener('load', startCamera);

document.getElementById('switchCamera').addEventListener('click', () => {
    useRearCamera = !useRearCamera; // Toggle between front and rear cameras
    startCamera();
});
