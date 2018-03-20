$(function () {
    updateViewList();
});

function updateViewList() {
    if (views.length === 0) {
        document.getElementById('view-table').innerHTML = "No Views found";
        return;
    }

    var html = '<table class="uk-table uk-table-striped">';
    html += '<tr>';
    html += '<th>View Name</th>';
    html += '</tr>';
    for (i in views) {
        html += '<tr>';
        html += '<td><a href=' + views[i]['name'] + '>';

        html += views[i]['name']
        html += '<iframe src="' + baseUrl + '/' + views[i]['name'] + '"></iframe>';

        html += '</a></td>';
        html += '</tr>';
    }


    html += '</table>';
    document.getElementById('view-table').innerHTML = html;
}
