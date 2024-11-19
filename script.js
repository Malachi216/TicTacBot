document.getElementById('upload-button').addEventListener('click', async () => {
    const fileInput = document.getElementById('game-image');
    const outputImg = document.getElementById('predicted-move');

    if (fileInput.files.length === 0) {
        alert('Please upload an image!');
        return;
    }

    const file = fileInput.files[0];

    // Simulate sending the file to the backend and getting the prediction
    const formData = new FormData();
    formData.append('image', file);

    try {
        // Send to the backend (adjust the URL as needed)
        const response = await fetch('https://your-backend-service/api/predict', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error('Failed to predict');
        }

        const data = await response.json();
        outputImg.src = data.predictedImageUrl; // The URL of the generated image
        outputImg.style.display = 'block';
    } catch (error) {
        console.error(error);
        alert('Error predicting the next move.');
    }
});