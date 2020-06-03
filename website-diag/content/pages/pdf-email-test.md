title: PDF Email test

<div id="pdf-requested" class="mt-5 alert alert-info" style="display: none;">
    <h3>PDF sent</h3>
    <p>An email message containing a code and instructions to download the following paper has been sent to your email address.</p>
</div>
<div id="pdf-error" class="mt-5 alert alert-warning" style="display: none;"></div>

Use the form below to request a PDF of bibkey "Bult20".

<form id="pdf-form" name="pdf-form">
    <input type="hidden" value="bult20" name="bibkey">
    <label for="email">
        Email:
    </label>
    <input type="email" id="email" name="email">

    <button type="submit">Request pdf</button>
</form>

<script>

const form = document.getElementById("pdf-form");
form.addEventListener("submit", function(event) {

    // Prevent normal form submit
    event.preventDefault();

    const data = new FormData(form);
    const params = new URLSearchParams(data).toString();

    fetch(`https://n3vxoalwka.execute-api.eu-west-3.amazonaws.com/default/sendpdf?${params}`, {
        method: 'GET',
        cache: 'no-cache'
    })
    .then(response => {
        switch(response.status) {
            case 404:
                throw new Exception("A pdf could not be found for this bibkey.");
            case 400:
                throw new Exception("The submitted information is not correct, please check your email address.");
            case 500:
                throw new Exception("The PDF service is currently unavaiable, please check again later.")
            default:
                return response;
        }
    })
    .then(() => {
        document.getElementById("pdf-requested").style.display = 'block';
        form.style.display = 'none';
    })
    .catch(error => {
        const errorEl = document.getElementById("pdf-error");
        errorEl.textContent = error.toString();
        errorEl.style.display = "block";
    });
});
</script>
