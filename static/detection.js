document.addEventListener("DOMContentLoaded", () => {

    const uploadArea = document.getElementById("uploadArea");
    const fileInput = document.getElementById("fileInput");
    const imagePreview = document.getElementById("imagePreview");
    const previewContainer = document.getElementById("previewContainer");
    const analyzeBtn = document.getElementById("analyzeBtn");

   
    uploadArea.addEventListener("click", () => {
        fileInput.value = ""; // reset file input
        fileInput.click();
    });

   
    fileInput.addEventListener("change", function () {

        
        imagePreview.src = "";
        previewContainer.innerHTML = "";

        const file = this.files[0];

        if (file) {
            const reader = new FileReader();

            reader.onload = function (e) {
                imagePreview.src = e.target.result;
                previewContainer.innerHTML = `<img src="${e.target.result}" width="200">`;
            };

            reader.readAsDataURL(file);
        }
    });

    
    analyzeBtn.addEventListener("click", function () {

        if (!fileInput.files.length) {
            alert("Please upload image first!");
            return;
        }

       
        document.getElementById("result").innerHTML = "";

        const formData = new FormData();
        formData.append("image", fileInput.files[0]);

        fetch("/predict", {
            method: "POST",
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            document.getElementById("result").innerHTML =
                "Prediction: " + data.prediction;
        })
        .catch(err => console.log(err));
    });

});