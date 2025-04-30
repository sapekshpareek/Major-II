import { Avatar, Box, Button, Popover, Typography } from '@mui/material';
import { useState } from 'react';
import toast from 'react-hot-toast';
import { useAuth } from '../context/AuthContext';

const Navbar = () => {
  const { user, logout } = useAuth();
  const [anchorEl, setAnchorEl] = useState(null);

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleLogout = async () => {
    try {
      await logout();
      handleClose();
      toast.success('Successfully logged out!');
    } catch (error) {
      console.error('Logout error:', error);
      toast.error('Failed to logout. Please try again.');
    }
  };

  const open = Boolean(anchorEl);

  return (
    <Box
      sx={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: '10px 20px',
        backgroundColor: '#fddfff',
        boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
        position: 'relative',
        zIndex: 1000,
      }}
    >
      <Typography variant="h6">Creating BNS Helper Using NLP</Typography>
      
      {user && (
        <>
          <Avatar
            onClick={handleClick}
            sx={{ 
              cursor: 'pointer',
              '&:hover': { opacity: 0.8 }
            }}
            src={user.picture}
          />
          <Popover
            open={open}
            anchorEl={anchorEl}
            onClose={handleClose}
            anchorOrigin={{
              vertical: 'bottom',
              horizontal: 'right',
            }}
            transformOrigin={{
              vertical: 'top',
              horizontal: 'right',
            }}
          >
            <Box sx={{ p: 2, minWidth: '200px' }}>
              <Typography variant="body1" sx={{ mb: 1 }}>{user.name}</Typography>
              <Typography variant="body2" sx={{ mb: 2, color: 'gray' }}>
                {user.email}
              </Typography>
              <Button 
                variant="contained" 
                onClick={handleLogout}
                fullWidth
                sx={{
                  backgroundColor: '#f00005',
                  '&:hover': { backgroundColor: '#d00004' }
                }}
              >
                Logout
              </Button>
            </Box>
          </Popover>
        </>
      )}
    </Box>
  );
};

export default Navbar; 