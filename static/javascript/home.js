const data = {
    kids: [
        { name: "Infants", slug: "infants" },
        { name: "Junior", slug: "junior" },
        { name: "Young", slug: "young" }
    ],
    adults: [
        { name: "Classic Novels", slug: "classic-novels" },
        { name: "Fiction", slug: "fiction" },
        { name: "Comic", slug: "comic" },
        { name: "Crime and Thriller", slug: "crime-and-thriller" }
    ]
};

const subcategoryGroup = document.getElementById("subcategory-group");

document.getElementById("category").addEventListener("change", function () {
    const category = this.value;
    const sub = document.getElementById("subcategory");

    sub.innerHTML = '<option value="">-- Select --</option>';

    if (!category) {
        subcategoryGroup.style.display = "none";
        return;
    }

    subcategoryGroup.style.display = "block";

    data[category].forEach(item => {
        const option = document.createElement("option");
        option.value = item.slug;      
        option.textContent = item.name;
        sub.appendChild(option);
    });
});


document.getElementById("subcategory").addEventListener("change", function () {
    const slug = this.value;
    if (!slug) return;
    window.location.href = `/books/${slug}`;
});