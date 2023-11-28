<script setup>
import { ref, reactive } from 'vue';


const props = defineProps({
    field: {
        type: String,
        default: null
    },
    header: {
        type: String,
        default: null
    },
    body: {
    },
    Name: {
        type: String
    },
    data: {
    },

});
</script>

<template>  
    <Column :field="props.field" :header="props.header" :sortable="true" headerStyle="width:14%; min-width:10rem;">
        <template :#body="props.body">
            <span class="p-column-title">{{props.Name}}</span>
            hola
            {{ props.data }}
        </template>
    </Column>
</template>