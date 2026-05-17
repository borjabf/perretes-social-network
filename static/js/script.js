// It ensures that the HTML has loaded
document.addEventListener("DOMContentLoaded", function () {
    // DOM selectors
    const textarea = document.getElementById('id_content'); // Bark textarea
    const counter = document.getElementById('char-counter'); // Char counter
    const submitBtn = document.getElementById('btn-submit-bark'); // Bark submit button
    const maxLength = 140; // Max length char allowed by requirements

    // Listener to track the live char length in the textarea
    textarea.addEventListener('input', function () {
        // Tracks the live char length in the textarea
        const currentLength = textarea.value.length;

        // Updates the content of the char counter with the live char length
        counter.textContent = currentLength

        /* Check the character count against the 140-character limit.
        If it exceeds this limit, notify the user visually;
        if not, you can send the Bark */
        if (currentLength > maxLength) {
            counter.style.color = 'red';
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.5';
        } else {
            counter.style.color = 'inherit';
            submitBtn.disabled = false;
            submitBtn.style.opacity = '1';
        }
    })
})