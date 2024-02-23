import { Hub } from "@/components/hubnav/hub";
import { Navbar } from "@/components/navcomponents/navbar";
import { Input } from "@/components/ui/input";
import { Separator } from "@/components/ui/separator";
import Image from "next/image";

export default function Home () {
    return(
        <div>
            <Navbar/>
            <div className="grid sm:grid-cols-4 sm:grid-rows-1 grid-cols-1 grid-rows-2 z-50">
                <div className="">
                    <Image
                    src="/images/doc.png"
                    width={400}
                    height={400}
                    alt="docimg"/>
                </div>
                <div className="text-end column-start-3">
                    <h3>One Stop Solution for all</h3>
                    <h3>your Health needs</h3>
                </div>
            </div>
        </div>
    )
}