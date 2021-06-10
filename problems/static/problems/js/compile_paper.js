const cartName = "problems_cart"

function fillSelectedProblemsForm() {
    const selectedInput = document.getElementById('selectedProblems')
    const storage = JSON.parse(localStorage.getItem(cartName)) || [];

    selectedInput.value = storage.join(' ');
}

function createSortable() {
    new Sortable(document.getElementById('selectedProblemsList'), {
        group: 'shared',
        animation: 150,
        ghostClass: 'bg-light',
        handle: '.fa-arrows-alt',
        scrollSensitivity: 100,

        onSort: function (/**Event*/evt) {
            const cart = JSON.parse(localStorage.getItem(cartName)) || [];
            const oldIndex = evt.oldIndex;
            const newIndex = evt.newIndex;

            const el = cart[oldIndex];
            cart.splice(oldIndex, 1);
            cart.splice(newIndex, 0, el);

            localStorage.setItem(cartName, JSON.stringify(cart));
        }
    })
}

function loadCart() {
    const cart = JSON.parse(localStorage.getItem(cartName)) || [];
    const cartData = {
        'selectedProblems': cart.join(' '),
    };
    const request = new Request(
        '',
        {headers: {'X-CSRFToken': CSRF_TOKEN}}
    );
    fetch(request, {
        method: 'POST',
        mode: 'same-origin',
        body: JSON.stringify(cartData)
    }).then(resPromise => {
        resPromise.text().then(result => {
            const mainDiv = document.getElementById('mainDiv')
            mainDiv.innerHTML = result;
            createSortable();
            renderMathInElement(mainDiv, {
                // customised options
                // • auto-render specific keys, e.g.:
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false},
                    {left: '\\(', right: '\\)', display: false},
                    {left: '\\[', right: '\\]', display: true}
                ],
                // • rendering keys, e.g.:
                throwOnError: false
            });
        })
    });
}

loadCart();

