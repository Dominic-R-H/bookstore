async function getOrders() {
    const errorMsg = document.getElementById("error-msg");

    errorMsg.innerText = "";

    try {
        const response = await fetch("/api/orders");

        const data = await response.json();

        if (!response.ok) {
            errorMsg.innerText = data.error;
            return;
        }
        
        const table = document.getElementById("orders-table");
        const tbody = document.getElementById("orders-body");

        tbody.innerHTML = "";

        data.orders.forEach(order => {
            const row = `
            <tr>
                <td>${order.order_id}</td>
                <td>${order.name}</td>
                <td>${order.email}</td>
                <td>${order.phone}</td>
                <td>${order.title}</td>
                <td>${order.price}</td>
            </tr>
        `;
            tbody.innerHTML += row;
        });

        table.style.display = "table";

    } catch (err) {
        console.log(err)
        errorMsg.innerText = "Something went wrong";
    }
}
