import React, { useState } from 'react'
import './CSS/Upload.css'
import { MdCloudUpload , MdDelete } from 'react-icons/md'
import { AiFillFileImage } from 'react-icons/ai'

const Upload = () => {
  const [image,setImage] = useState(null)
  const [fileName, setFileName ] = useState('No selected file')
  return (
    <div className='upload'>
      <h1>Upload your picture</h1>
      <p>In this section, you can upload photos of your cars so </p>
      <p>that this artificial intelligence can show the weaknesses</p>
      <p>of the car's body and color.</p> 
      <form action=""
      onClick={() => document.querySelector('.input-field').click()}
      >


        <input type="file" accept= 'image/*' className='input-field' hidden
        
        onChange={({target: {files}}) =>{
          files[0] && setFileName(files[0].name)
          if (files){
            setImage(URL.createObjectURL(files[0]))
          }
        }}

        
        />
        {image ? (
        <img src={image} width={150} height={150} alt={fileName} />
        ):(
        <><MdCloudUpload color='#1475cf' size={60}/>
        <p>Browse Files to Upload</p>
        </>
        
        
        )}
  
      </form>

      <section className='uploaded-row'>
          <AiFillFileImage color='#1475cf'/>
          <span>
            {fileName}
            <MdDelete
            onClick={() => {
              setFileName('No Selected File')
              setImage(null)
            }}/>
          </span>
            
      </section>

    </div>
  )
}

export default Upload
 