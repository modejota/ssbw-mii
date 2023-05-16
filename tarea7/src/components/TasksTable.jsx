import { Button, TextField } from '@mui/material';
import { styled } from '@mui/material/styles';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';

// STYLES
const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 14,
  },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  '&:nth-of-type(odd)': {
    backgroundColor: theme.palette.action.hover,
  }
}));

const AddTaskSectionStyles = {
  container: {
    display: 'flex',
    alignItems: 'center',
    marginTop: '1vh',
    marginBottom: '1vh',
    marginLeft: '1.5vw',
  },
  button: {
    marginLeft: '10px',
  },
};


// COMPONENTS
const TableHeader = () => {
  return (
    <TableHead>
      <TableRow>
        <StyledTableCell align='center'>Task</StyledTableCell>
        <StyledTableCell align='center'>Status</StyledTableCell>
        <StyledTableCell align='center'></StyledTableCell>
      </TableRow>
    </TableHead>
  );
};

const MyTableBody = ({ tasks, handleDelete, changeTaskStatus }) => {
  const rows = tasks.map((row, index) => {
    return (
      <StyledTableRow key={index}>
        <StyledTableCell component="th" scope="row" align='center'>{row.title}</StyledTableCell>
        <StyledTableCell align="center">{row.status}</StyledTableCell>
        <StyledTableCell align="center">
          <Button variant='contained' color='primary' size='small' onClick={() => changeTaskStatus(index)}>Change Status</Button>
          <span style={{ marginRight: '1.5vw' }}></span>
          <Button variant='contained' color='error' size='small' onClick={() => handleDelete(index)}>Delete</Button>
        </StyledTableCell>
      </StyledTableRow>
    );
  });
  return <TableBody>{rows}</TableBody>
};

const AddTaskSection = ({ textFieldValue, handleTextFieldChange, handleAdd }) => {
  return (
    <div style={AddTaskSectionStyles.container}>
      <TextField id="outlined-basic" label="Task to be done" variant="outlined"
        value={textFieldValue} onChange={handleTextFieldChange} />
      <Button variant='contained' color='success' style={AddTaskSectionStyles.button} onClick={handleAdd}>Add Task</Button>
    </div>
  );
};

const TasksTable = ({ tasks, handleDelete, changeTaskStatus, handleAdd, textFieldValue, handleTextFieldChange }) => {
  return (
    <div>
      <Table sx={{ minWidth: 700 }} aria-label="customized table">
        <TableHeader />
        <MyTableBody tasks={tasks} handleDelete={handleDelete} changeTaskStatus={changeTaskStatus} />
      </Table>
      <AddTaskSection textFieldValue={textFieldValue} handleTextFieldChange={handleTextFieldChange} handleAdd={handleAdd} />
    </div>
  );
}

export default TasksTable;