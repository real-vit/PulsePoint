import { Hub } from "@/components/hubnav/hub";
import Link from "next/link";
import { DocShow } from "./testcenters/testcenters";
import { Separator } from "@/components/ui/separator";

export default function Home () {
    return(
        <div className="mx-auto items-center">
            <Hub/>
            <br />
            <div className="relative">
                <div className="bg-green-300 w-full h-32">
                    <p className="font-lg sm:font-3xl font-bold">
                        Submit the PDF of your blood report here...</p>
                    {/* Add pdf uploading stuff */}
                    <br />
                    <div className="h-92 w-92 border-black border-5 items-center text-center px-10">
                        <Link href="/">
                            <div className="border-dotted border-black border-2 px-5">
                                Upload Here...
                            </div>
                            
                        </Link>
                        
                        
                        
                    </div>
                </div>
                <Separator/>
                <h2 className="font-bold font-3xl text-center">OR Search a Test Center Near You...</h2>
                <br />
                <br />
                <br/>
                <br/>
                <DocShow/>
            </div>
        </div>
        
    )
}