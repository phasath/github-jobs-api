var apiLanguage = ""
var apiLocation = ""

function changeLanguage(event) {
    const label = $(event).text()
    apiLanguage = label !== "Language" ? label.toLowerCase() : ""
    let btn = $('#languageButton')
    btn.html(label)
    queryAPI()
}

function changeLocation(event) {
    const label = $(event).text()
    apiLocation = label !== "Location" ? label.toLowerCase() : ""
    let btn = $('#locationButton')
    btn.html(label)
    queryAPI()
}

get_company = (obj) => {
    if (obj.company_url === "" || obj.company_url === "http:" || obj.company_url === "http://http" || obj.company_url == null) {
        return null
    } else {
        return obj.company_url.replace(/(^\w+:|^)\/\//, '')
    }
}
get_fulltime = (obj) => obj.fulltime == true ? "Yes" : "No"

function threatData(data) {
    return data.map(cur => ({...cur, company_url: get_company(cur), fulltime: get_fulltime(cur) }))
}

function generateHTML(data) {
    htmltxt = `<html><head><title>${data.company}</title></head><body>
    <header>
        <img src="${data.company_logo}" alt="${data.company} logo" style="max-width:150px;max-height:150px">
        <h1>${data.company}</h1>
        <p><a href="http://${data.company_url != null ? data.company_url : ""}">${data.company_url != null ? data.company_url : ""}</a></p>
    </header>
    <h2>Title: ${data.title}</h2>
    <h2>Available since: ${data.created_at}</h2>
    <h2>Is fulltime: ${data.fulltime}</h2>
    <h2>Location: ${data.location}</h2>

    <h2>Description:<h2>
    <span>${data.description}</span>

    <h2>How to Apply:<h2>
    <span>${data.how_to_apply}</span>
    `
    return htmltxt
}

function changeTableData(data) {
    threatedData = threatData(data)
    let table = $('#dataTable').DataTable();

    table.clear();
    table.rows.add(threatedData);
    table.draw();

    $('#dataTable tbody').on('click', 'tr', function() {
        let data = table.row(this).data();
        let jobWindow = window.open("", "newWindow", "width=500,height=700");
        jobWindow.document.write(generateHTML(data));
    });
}

function queryAPI() {
    const pathLocation = apiLocation ? `location=${apiLocation}` : ''
    const pathLanguage = apiLanguage ? `language=${apiLanguage}` : ''
    $.ajax({
        type: "GET",
        url: `/api/jobs?${pathLocation}&${pathLanguage}`,
        success: changeTableData,
        error: function(req, textStatus, errorThrown) {
            alert(`Something unexpected happened: ${textStatus} - ${errorThrown}`)
        },
        dataType: "json"
    });
}


$(function() {
    $(document).ready(function() {
        $('[data-toggle-second="tooltip"]').tooltip()
        $('.toast').toast()
        $('#dataTable').DataTable({
            "info": true,
            "columns": [
                // { "data": "id", "title": "ID", "width": "70px" },
                { "data": "company", "title": "Company", "width": "70px" },
                // { "data": "company_logo", "title": "Company Logo", "width": "100px" },
                { "data": "company_url", "title": "Company URL", "width": "90px" },
                { "data": "created_at", "title": "Available Since", "width": "70px" },
                // { "data": "description", "title": "Description", "width": "70px" },
                { "data": "fulltime", "title": "Fulltime", "width": "70px" },
                // { "data": "how_to_apply", "title": "How to Apply", "width": "90px" },
                { "data": "location", "title": "Location", "width": "70px" },
                { "data": "title", "title": "Title", "width": "70px" }
            ],
        })
        queryAPI()
    });
});