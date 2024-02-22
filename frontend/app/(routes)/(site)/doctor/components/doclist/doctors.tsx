import Image from "next/image";

export const DoctorData = ({
    name,img,spl}:{
        name: string;
        img: string;
        spl: string
    }
)=>{
    return(
        <div className="absolute items-start w-full h-32 border-3 border-black px-7 py-7 grid grid-cols-4">
            <div className="absolute self-start">
                 <Image
                src={img}
                width={200}
                height={200}
                alt={name}
                /> 
            </div>
            <div className="font-bold  col-start-3 md:col-start-2 md:col-end-4">
                <h2 className="md:text-3xl text-xl">{name}</h2>
                <p className="text-md">{spl}</p>
            </div>
            <br/>
            <br />
        </div>
    )
}
