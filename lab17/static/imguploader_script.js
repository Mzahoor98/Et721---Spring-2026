const uploadForm = document.querySelector('#uploadform')
const message = document.querySelector('#message')
const gallery = document.querySelector('#gallery')

uploadForm.addEventListener('submit', function (e) {
    e.preventDefault()

    const fileInput = document.querySelector('#imageInput')

    if (!fileInput.files.length) {
        message.textContent = 'Please select an image to upload.'
        message.style.color = 'red'
        return
    }

    const formData = new FormData()
    formData.append('image', fileInput.files[0])

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                message.textContent = data.message
                message.style.color = 'green'
                setTimeout(() => { location.reload() }, 1000)
            } else {
                message.textContent = data.error || 'Upload failed.'
                message.style.color = 'red'
            }
        })
        .catch(error => {
            message.textContent = 'Upload failed.'
            message.style.color = 'red'
            console.error('Upload error:', error)
        })
})

gallery.addEventListener('click', function (e) {
    if (!e.target.classList.contains('btndelete')) return

    const imageId = e.target.dataset.id
    deleteImage(imageId)
})

function deleteImage(id) {
    if (!confirm('Are you sure you want to delete this image?'))
        return

    fetch(`/delete/${id}`, {
        method: 'DELETE'
    })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                const imageCard = document.getElementById(`image-${id}`)
                if (imageCard) imageCard.remove()
            } else {
                alert(data.error)
            }
        })
        .catch(error => {
            alert('Delete failed: ' + error)
            console.error('Delete error:', error)
        })
}
