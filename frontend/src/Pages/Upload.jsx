import React, { useState } from 'react'
import './CSS/Upload.css'
import { MdCloudUpload, MdDelete } from 'react-icons/md'
import { AiFillFileImage } from 'react-icons/ai'
import img_ from '/home/reza/Vision/SoftWareDesign/Window/frontend/src/Components/Assets/pred_res.png'
const Upload = () => {
  const [image, setImage] = useState(null)
  const [fileName, setFileName] = useState('No selected file')
  const [resultImage, setResultImage] = useState(null)

  const handleImageUpload = async (files) => {
    
    if (files[0]) {
      const formData = new FormData()
      formData.append('image', files[0])

      setFileName(files[0].name)
      setImage(URL.createObjectURL(files[0]))

      try {
        const response = await fetch('http://localhost:8000/api/predict/', {
          method: 'POST',
          body: formData
        })
        const data = await response.json()
        console.log('Response:', data)
        setTimeout(() => {
          setResultImage(img_)

        }, 2000)

      } catch (error) {
        console.log('Error:', error)
      }
    }
  }

  return (
    <div className='upload'>
      <h1>Upload your picture</h1>
      <p>In this section, you can upload photos of your cars so </p>
      <p>that this artificial intelligence can show the weaknesses</p>
      <p>of the car's body and color.</p> 
      
      <form onClick={() => document.querySelector('.input-field').click()}>
        <input 
          type="file" 
          accept='image/*' 
          className='input-field' 
          hidden
          onChange={({target}) => handleImageUpload(target.files)}
        />
        
        {image ? (
          <img src={image} width={150} height={150} alt={fileName} />
        ) : (
          <>
            <MdCloudUpload color='#1475cf' size={60}/>
            <p>Browse Files to Upload</p>
          </>
        )}
      </form>

      {resultImage && (
        <div className="result-container">
          <h3>AI Detection Result:</h3>
          <img src={resultImage} alt="AI Detection" style={{maxWidth: '400px', height: 'auto'}} />
          
        </div>
      )}

      <section className='uploaded-row'>
        <AiFillFileImage color='#1475cf'/>
        <span>
          {fileName}
          <MdDelete
            onClick={() => {
              setFileName('No Selected File')
              setImage(null)
              setResultImage(null)
            }}
          />
        </span>
      </section>
    </div>
  )
}

export default Upload