"use client";
import { Box, Link, Typography } from '@mui/material';

const Footer = () => {
  return (
    <Box
      component="footer"
      sx={{
        display: 'flex',
        flexDirection: { xs: 'column', sm: 'row' },
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: '20px',
        backgroundColor: '#fddfff',
        borderTop: '1px solid rgba(0, 0, 0, 0.1)',
        width: '100%',
        marginTop: 'auto',
        position: 'relative',
        bottom: 0
      }}
    >
      <Box
        sx={{
          display: 'flex',
          flexDirection: { xs: 'column', sm: 'row' },
          alignItems: 'center',
          gap: 2,
          mb: { xs: 2, sm: 0 },
        }}
      >
        <Typography variant="body2" color="text.primary">
          © 2024 Stormborn Software. All rights reserved.
        </Typography>
      </Box>

      <Box
        sx={{
          display: 'flex',
          gap: 3,
          flexWrap: 'wrap',
          justifyContent: 'center',
        }}
      >
        <Link
          href="/privacy"
          sx={{
            color: 'text.primary',
            textDecoration: 'none',
            '&:hover': { color: '#f00005' }
          }}
        >
          <Typography variant="body2">
            Privacy Policy
          </Typography>
        </Link>

        <Link
          href="/terms"
          sx={{
            color: 'text.primary',
            textDecoration: 'none',
            '&:hover': { color: '#f00005' }
          }}
        >
          <Typography variant="body2">
            Terms of Service
          </Typography>
        </Link>

        <Link
          href="mailto:info@stormborn.onmicrosoft.com"
          sx={{
            color: 'text.primary',
            textDecoration: 'none',
            '&:hover': { color: '#f00005' }
          }}
        >
          <Typography variant="body2">
            Contact Us
          </Typography>
        </Link>
      </Box>
    </Box>
  );
};

export default Footer; 