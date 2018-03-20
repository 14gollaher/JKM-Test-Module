$(function () {
    updateViewList();
});

function updateViewList() {
    if (views.length === 0) {
        document.getElementById('view-table').innerHTML = "No Views found";
        return;
    }

    var html = '';
    for (i in views) {
        html += '<a href=' + views[i]['name'] + '>';
        html += '<div class="uk-card-default uk-card-hover uk-margin-medium-top uk-margin-medium-left uk-margin-medium-bottom">';
        html += '<h3 style="color: black; font-weight: bold;">' + views[i]['name'] + '</h3>';
        html += '<iframe class="uk-border-rounded" src="' + baseUrl + '/' + views[i]['name'] + '" style="width:90%; height:500px;"></iframe>';
        html += '</div>';
        html += '</a>';
    }
    for (i in views) {
        html += '<a href=' + views[i]['name'] + '>';
        html += '<div class="uk-card-default uk-card-hover uk-margin-medium-top uk-margin-medium-left uk-margin-medium-bottom">';
        html += '<h3 style="color: black; font-weight: bold;">' + views[i]['name'] + '</h3>';
        html += '<iframe class="uk-border-rounded" src="' + baseUrl + '/' + views[i]['name'] + '" style="width:90%; height:500px;"></iframe>';
        html += '</div>';
        html += '</a>';
    }
    for (i in views) {
        html += '<a href=' + views[i]['name'] + '>';
        html += '<div class="uk-card-default uk-card-hover uk-margin-medium-top uk-margin-medium-left uk-margin-medium-bottom">';
        html += '<h3 style="color: black; font-weight: bold;">' + views[i]['name'] + '</h3>';
        html += '<iframe class="uk-border-rounded" src="' + baseUrl + '/' + views[i]['name'] + '" style="width:90%; height:500px;"></iframe>';
        html += '</div>';
        html += '</a>';
    }
    for (i in views) {
        html += '<a href=' + views[i]['name'] + '>';
        html += '<div class="uk-card-default uk-card-hover uk-margin-medium-top uk-margin-medium-left uk-margin-medium-bottom">';
        html += '<h3 style="color: black; font-weight: bold;">' + views[i]['name'] + '</h3>';
        html += '<iframe class="uk-border-rounded" src="' + baseUrl + '/' + views[i]['name'] + '" style="width:90%; height:500px;"></iframe>';
        html += '</div>';
        html += '</a>';
    }
    

    document.getElementById('view-table').innerHTML = html;
}
