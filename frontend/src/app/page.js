"use client";

import Footer from "@/Components/Footer";
import Navbar from "@/Components/Navbar";
import { Typography } from "@mui/material";

export default function Home() {
  return (
    <div>
      <Navbar />
      <Typography variant= "h1"sx={{height: '82vh'}}>Hello</Typography>
      <Footer />
    </div>
  );
}
