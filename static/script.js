document.getElementById('swapBtn').addEventListener('click', () => {
    const src = document.getElementById('srcLang');
    const tgt = document.getElementById('tgtLang');
    [src.value, tgt.value] = [tgt.value, src.value];
});

async function translateText() {
    const text = document.getElementById('inputText').value;
    const srcLang = document.getElementById('srcLang').value;
    const tgtLang = document.getElementById('tgtLang').value;
    const status = document.getElementById('status');
    const output = document.getElementById('outputText');

    if (!text.trim()) {
        status.textContent = "Please enter some text.";
        output.value = "";
        return;
    }

    status.textContent = "Translating...";
    output.value = "";

    try {
        const response = await fetch("http://127.0.0.1:5000/translate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text,
                src_lang: srcLang,
                tgt_lang: tgtLang
            })
        });

        const data = await response.json();
        output.value = data.translation;
        status.textContent = "Translation completed!";
    } catch (error) {
        console.error(error);
        status.textContent = "Failed to translate.";
    }
}
