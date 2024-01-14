function nameSaver(name) {
    // var button_name = document.getElementById("name")
    console.log(name)
    url='https://store.ncss.cloud/group2/dnd/name/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: name
        })
    })
}