
function fetch_data(index) {
    $.getJSON('./stats.json', function (data) {
        let num = 0;
        $(".data-nav").empty();
        $(".data").empty();
        data.forEach((d, i) => {
            $(".data-nav").append(
                `
            <li class="nav-item">
            <a class="nav-link" href="#c-${i}">
                <span data-feather="file" class="align-text-bottom"></span>
                ${d.name}
            </a>
        </li>`
            );
        })

        if (index > data.length) {
            index = 0
        }
        data[index].results.sort((a, b) => { return a.elapse - b.elapse; }).forEach(d => {
            $(".data").append(`<tr><td>${num}</td><td>${d.name}</td><td>${d.build ? "yes" : "no"}</td><td>${d.elapse}</td></tr>`);
            ++num;
        });

        $("#name").text(`${data[index].name}`);
        $("#id").text(`${index + 1}`);

    });
}

fetch_data(0);


function locationHashChanged() {
    var index = parseInt(window.location.hash.substring(3))
    fetch_data(index);
}

window.onhashchange = locationHashChanged;