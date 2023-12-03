          const fileInput = document.getElementById('file-input');
          const uploadButton = document.getElementById('upload-button');

          uploadButton.addEventListener('click', () => {
            fileInput.click();
          });

          fileInput.addEventListener('change', () => {
            const file = fileInput.files[0];
          });
          