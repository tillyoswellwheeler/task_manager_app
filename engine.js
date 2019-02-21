
let url = 'http://127.0.0.1:5000/tasks';

get_api_data = fuction httpGet(url)
{
  var xmlHttp = new XMLHttpRequest();
  xhttp.open("GET", url, false);
  xhttp.send(null);
  return xmlHttp.responsetext;
};

let mock_json = {
  "task_id":"0001"
};

document.getelementById("api-resp").innerHTML = get_api_data(url)
