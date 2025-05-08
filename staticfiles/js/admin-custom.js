/**
 * Custom JavaScript for the Django Admin
 * Enhances admin forms and improves user experience
 */

document.addEventListener('DOMContentLoaded', function() {
    // Enhanced file input for image uploads
    enhanceImageUploadFields();
    
    // Add field descriptions tooltip
    addFieldDescriptionTooltips();
    
    // Add form validation enhancements
    enhanceFormValidation();
    
    // Improve the UI for related fields
    enhanceRelatedFieldsUI();
});

/**
 * Enhances image upload fields with preview functionality
 */
function enhanceImageUploadFields() {
    // Find all file inputs that are for images
    const imageFields = document.querySelectorAll('input[type="file"][name*="image"]');
    
    imageFields.forEach(function(field) {
        // Create a container for the preview
        const container = document.createElement('div');
        container.className = 'image-preview-container';
        
        // Create image preview element
        const preview = document.createElement('div');
        preview.className = 'image-preview';
        preview.innerHTML = `
            <p class="upload-prompt">Select an image to see preview</p>
            <img class="preview-image" style="display: none; max-width: 300px; max-height: 300px; margin-top: 10px; border-radius: 5px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
        `;
        
        // Insert the preview after the file input
        field.parentNode.insertBefore(container, field.nextSibling);
        container.appendChild(preview);
        
        // Add event listener for file selection
        field.addEventListener('change', function(e) {
            const file = this.files[0];
            const previewImg = preview.querySelector('.preview-image');
            const uploadPrompt = preview.querySelector('.upload-prompt');
            
            if (file) {
                const reader = new FileReader();
                
                reader.onload = function(e) {
                    previewImg.src = e.target.result;
                    previewImg.style.display = 'block';
                    uploadPrompt.style.display = 'none';
                };
                
                reader.readAsDataURL(file);
                
                // Add file name and size info
                const fileInfo = document.createElement('div');
                fileInfo.className = 'file-info';
                fileInfo.innerHTML = `
                    <p><strong>File:</strong> ${file.name}</p>
                    <p><strong>Size:</strong> ${formatFileSize(file.size)}</p>
                `;
                
                // Check if file info already exists and remove it
                const existingFileInfo = preview.querySelector('.file-info');
                if (existingFileInfo) {
                    preview.removeChild(existingFileInfo);
                }
                
                preview.appendChild(fileInfo);
            } else {
                previewImg.style.display = 'none';
                uploadPrompt.style.display = 'block';
                
                // Remove file info if exists
                const existingFileInfo = preview.querySelector('.file-info');
                if (existingFileInfo) {
                    preview.removeChild(existingFileInfo);
                }
            }
        });
        
        // Check if there's already an image (for edit pages)
        const existingImage = field.closest('.form-row').querySelector('a[href*="media"]');
        if (existingImage) {
            const previewImg = preview.querySelector('.preview-image');
            const uploadPrompt = preview.querySelector('.upload-prompt');
            
            // If there's an existing image, show it in the preview
            uploadPrompt.innerHTML = 'Current image (select a new one to replace):';
            const currentImg = document.createElement('img');
            currentImg.src = existingImage.href;
            currentImg.style.maxWidth = '300px';
            currentImg.style.maxHeight = '300px';
            currentImg.style.marginTop = '10px';
            currentImg.style.borderRadius = '5px';
            currentImg.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
            
            uploadPrompt.appendChild(currentImg);
        }
    });
}

/**
 * Helper function to format file size
 */
function formatFileSize(bytes) {
    if (bytes < 1024) return bytes + ' bytes';
    else if (bytes < 1048576) return (bytes / 1024).toFixed(1) + ' KB';
    else return (bytes / 1048576).toFixed(1) + ' MB';
}

/**
 * Add tooltip descriptions to form fields
 */
function addFieldDescriptionTooltips() {
    const helpTexts = document.querySelectorAll('.help');
    
    helpTexts.forEach(function(helpText) {
        const field = helpText.closest('.form-row').querySelector('input, select, textarea');
        if (field) {
            field.setAttribute('title', helpText.textContent.trim());
            field.classList.add('has-tooltip');
        }
    });
}

/**
 * Enhance form validation with better visual feedback
 */
function enhanceFormValidation() {
    const form = document.querySelector('#content-main form');
    if (!form) return;
    
    // Add validation class to required fields
    const requiredFields = form.querySelectorAll('input[required], select[required], textarea[required]');
    requiredFields.forEach(function(field) {
        field.addEventListener('blur', function() {
            if (!this.value.trim()) {
                this.classList.add('validation-error');
                // Add error message if it doesn't exist
                if (!this.nextElementSibling || !this.nextElementSibling.classList.contains('error-message')) {
                    const errorMsg = document.createElement('p');
                    errorMsg.className = 'error-message';
                    errorMsg.style.color = '#e74c3c';
                    errorMsg.style.fontSize = '12px';
                    errorMsg.style.marginTop = '5px';
                    errorMsg.textContent = 'This field is required.';
                    this.parentNode.insertBefore(errorMsg, this.nextSibling);
                }
            } else {
                this.classList.remove('validation-error');
                // Remove error message if exists
                if (this.nextElementSibling && this.nextElementSibling.classList.contains('error-message')) {
                    this.parentNode.removeChild(this.nextElementSibling);
                }
            }
        });
    });
}

/**
 * Improve UI for related fields (ForeignKey, ManyToMany)
 */
function enhanceRelatedFieldsUI() {
    // Make related object links open in a new tab
    const relatedLinks = document.querySelectorAll('.related-widget-wrapper a');
    relatedLinks.forEach(function(link) {
        link.setAttribute('target', '_blank');
        link.setAttribute('title', 'Open in new tab');
    });
}