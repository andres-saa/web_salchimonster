function formatDateForMySQL(date) {
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    return `${year}-${month}-${day}`;
  }

  function isValidDate(dateString) {
    const date = new Date(dateString);
    return !date instanceof Date;
  }
  
  function convertStringToDate(dateString) {
    let dateParts = dateString.split("-");
    let year = parseInt(dateParts[0]);
    let month = parseInt(dateParts[1]) - 1;
    let day = parseInt(dateParts[2]);
  
    let dateObject = new Date(year, month, day);
  
    return dateObject;
  }

  export {formatDateForMySQL,isValidDate,convertStringToDate}