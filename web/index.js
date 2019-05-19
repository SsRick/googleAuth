// Create the XHR object.
function createCORSRequest(method, url) {
    var xhr = new XMLHttpRequest();
    if ("withCredentials" in xhr) {
        // XHR for Chrome/Firefox/Opera/Safari.
        xhr.open(method, url, true);
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    } else if (typeof XDomainRequest != "undefined") {
        // XDomainRequest for IE.
        xhr = new XDomainRequest();
        xhr.open(method, url);
    } else {
        // CORS not supported.
        xhr = null;
    }
    return xhr;
}
// Make CORS request.
function sendrequest(url, thejson, callback) {
    //var url = 'https://fof0qebtce.execute-api.us-west-2.amazonaws.com/corstest';
    var xhr = createCORSRequest('POST', url);
    if (!xhr) {
        alert('CORS not supported');
        return;
    }
    xhr.onload = function() {
        var text = xhr.responseText;
        console.log(text);
        callback(text);
    };
    xhr.onerror = function() {
        alert('Error making the request.');
    };
    xhr.send(JSON.stringify(thejson));
}
const formToJSON = elements => [].reduce.call(elements, (data, element) => {
    data[element.name] = element.value;
    return data;
}, {});

function getloginurl() {
    const form = document.getElementsByClassName('theform')[0];
    const data = formToJSON(form.elements);
    myjson = sendrequest(url = 'https://fof0qebtce.execute-api.us-west-2.amazonaws.com/postCorTest', data, function(response) {
        var obj = JSON.parse(response);
        console.log(obj.url);
        window.open(obj.url)
    });
}

function exchangetoken() {
    const form = document.getElementsByClassName('theform')[0];
    const data = formToJSON(form.elements);
    myjson = sendrequest(url = 'https://kdl7hllpzh.execute-api.us-west-2.amazonaws.com/testing', data, function(response) {
        var obj = JSON.parse(response);
        
        document.getElementById("json").innerHTML = JSON.stringify(obj, undefined, 2);
    });
}

function refeshtoken() {
    const form = document.getElementsByClassName('theform')[0];
    const data = formToJSON(form.elements);
    myjson = sendrequest(url = 'https://udcoamskfi.execute-api.us-west-2.amazonaws.com/refreshing', data, function(response) {
        var obj = JSON.parse(response);
        
        document.getElementById("json").innerHTML = JSON.stringify(obj, undefined, 2);
    });
}