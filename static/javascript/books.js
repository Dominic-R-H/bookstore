document.addEventListener("DOMContentLoaded", function () {

    const subcategory = window.location.pathname.split("/").pop();
    const container = document.getElementById("books-container");

    if (!subcategory) {
        container.innerHTML = "<p>No books for this subcategory.</p>";
        return;
    }

    fetch(`/api/books/${subcategory}`)
        .then(res => res.json())
        .then(data => {

            const books = data.books;
            const loggedIn = data.logged_in;

            if (!books || books.length === 0) {
                container.innerHTML = "<p>No books for this subcategory.</p>";
                return;
            }

            container.innerHTML = "";

            books.forEach(book => {
                const card = document.createElement("div");
                card.className = "book__card";

                card.innerHTML = `
                    <img class="book__image" src="${book.image}"  alt="Buy ${book.title} book online" loading="lazy">

                    <div class="book__info">
                        <div class="book__title">${book.title}</div>
                        <div class="book__price">$${book.price}</div>
                    </div>
                `;

                if (loggedIn) {
                    const btn = document.createElement("button");
                    btn.className = "book__buy";
                    btn.innerText = "Place Order";

                    btn.onclick = function () {
                        fetch("/api/order", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify({ book_id: book.id })
                        })
                            .then(res => res.json())
                            .then(data => {
                                if (data.order_id) {
                                    alert("Congratulations! Your order has been placed.\nYour order id is: " + data.order_id);
                                } else {
                                    alert("Failed to place order");
                                }
                            })
                            .catch(() => alert("Failed to place order"));
                    };

                    card.querySelector(".book__info").appendChild(btn);
                }
                container.appendChild(card);
            });
        })
        .catch(_ => {
            console.log(_);
            container.innerHTML = "<p>Error loading books.</p>";
        });
});