import * as React from "react"
import Image from "next/image"

import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"
import Link from "next/link"

export interface Artwork {
  artist: string
  art: string
  link: string
}

export const works: Artwork[] = [
  {
    artist: "Ornella Binni",
    art: "/images/pill.jpg",
    link: "/",
  },
  {
    artist: "Tom Byrom",
    art: "/images/pill.jpg",
    link: "/",
  },
  {
    artist: "Vladimir Malyavko",
    art: "/images/pill.jpg",
    link: "/",
  },
  {
    artist: "Vladimir Malyavko",
    art: "/images/pill.jpg",
    link: "/",
  },
  {
    artist: "Vladimir Malyavko",
    art: "/images/pill.jpg",
    link: "/",
  }
]

export function Scroll() {
  return (
    <ScrollArea className="w-full h-100 whitespace-nowrap rounded-md border">
      <div className="flex w-max space-x-4 p-4">
        {works.map((artwork) => (
          <figure key={artwork.artist} className="shrink-0">
            <Link className="overflow-hidden rounded-md" href="/">
              <Image
                src={artwork.art}
                alt={`Photo by ${artwork.artist}`}
                className="aspect-[3/4] h-fit w-fit object-cover"
                width={90}
                height={90}
              />
            </Link>
            <figcaption className="pt-2 text-xs text-muted-foreground">
              <span className="font-semibold text-foreground">
                {artwork.artist}
              </span>
            </figcaption>
          </figure>
        ))}
      </div>
      <ScrollBar orientation="horizontal" />
    </ScrollArea>
  )
}
