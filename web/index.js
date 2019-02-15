// Create the XHR object.
function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
    // XHR for Chrome/Firefox/Opera/Safari.
    xhr.open(method, url, true);
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
function sendrequest(url, callback) {
  //var url = 'https://fof0qebtce.execute-api.us-west-2.amazonaws.com/corstest';

  var xhr = createCORSRequest('GET', url);
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

  xhr.send();
}

function openaws() {
   sendrequest(url = 'https://fof0qebtce.execute-api.us-west-2.amazonaws.com/corstest', function(response){
      var obj = JSON.parse(response);
      console.log(obj.url);
      //open the url in the same tab
      window.location.replace(obj.url);
   });
   
}
