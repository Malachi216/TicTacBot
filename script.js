const upload = document.getElementById('upload');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const download = document.getElementById('download');

upload.addEventListener('change', (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function () {
        const img = new Image();
        img.src = reader.result;

        img.onload = function () {
            // Set canvas dimensions to match the image
            canvas.width = img.width;
            canvas.height = img.height;

            // Draw the image on the canvas
            ctx.drawImage(img, 0, 0);

            // Apply a simple filter (e.g., grayscale)
            const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const data = imageData.data;

            for (let i = 0; i < data.length; i += 4) {
                const avg = (data[i] + data[i + 1] + data[i + 2]) / 3;
                data[i] = avg; // Red
                data[i + 1] = avg; // Green
                data[i + 2] = avg; // Blue
            }

            ctx.putImageData(imageData, 0, 0);

            // Enable the download button
            download.disabled = false;
        };
    };

    reader.readAsDataURL(file);
});

download.addEventListener('click', () => {
    const link = document.createElement('a');
    link.download = 'processed-image.png';
    link.href = canvas.toDataURL();
    link.click();
});
