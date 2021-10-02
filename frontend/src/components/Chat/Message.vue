<template>
    <div class="message mt-3" :class="right ? 'message__right-parent' : 'message__left-parent'">
        <div class="message__pre-child w-100" v-if="showGraph">
            <apexchart v-if="right" width="100"  :options="options" :series="series"></apexchart>
            <div class="message__child" :class="right ? 'message__right' : 'message__left'">
                <div class="message__header">
                    {{ name }}
                </div>
                <div class="message__content">
                    {{ content }}
                </div>
            </div>
            <apexchart v-if="!right" width="100"  :options="options" :series="series"></apexchart>
            
        </div>
        <div class="message__child" :class="right ? 'message__right' : 'message__left'" v-else>
            <div class="message__header">
                {{ name }}
            </div>
            <div class="message__content">
                {{ content }}
            </div>
        </div>
    </div>
</template>

<script>
import {computed} from "vue"

export default {
    props: {
        right: Boolean,
        content: String,
        name: String,
        labels: Object
    },
    setup(props){
        const options = {
            chart: {
                type: "donut"
            },
            plotOptions: {
                pie: {
                    customScale: 1,
                    donut: {
                        labels: {
                            show: false,
                            name: {
                                show: false,
                            },
                            value: {
                                show: false,
                            },
                        },
                    },
                },
            },
            fill: {
                opacity: 1,
            },
    
            colors: ["#30f615", "#FFB801", "#c60303"],
    
            dataLabels: {
                enabled: false,
            },
            legend: {
                show: false
            }
        }
        
        
        const series = computed(() => {
            if (props.labels){
                console.log(props.labels)
                return [props.labels.neg, props.labels.neu, props.labels.pos]
            }
            return []
        })
        
        const showGraph = computed(() => {
            if (props.labels) {
                console.log(props.labels)
                if (props.labels.neg > 0 || props.labels.neu > 0 || props.labels.pos > 0){
                    return true
                }
            }
            return false
        })
        
        return {
            options,
            series,
            showGraph
        }
    }
}
</script>

<style lang="scss">
.message {
    display: flex;
    
    //max-width: calc(100% - 5.5625rem);
    
    &__header {
        padding: 5px 9px 0 9px;
        font-weight: 500 !important;
        font-size: .9rem;
        color: rgb(252, 92, 81);
    }
    &__child {
        position: relative;
        border-radius: 6px 12px 12px 6px;
        //display: flex;
        max-width: calc(100% - 5.5625rem);
    }
    &__content {
        padding: 0 .5rem .375rem .625rem;
        line-height: 1.3125;
        word-break: break-word;
        white-space: pre-wrap;
    }
    
    &__pre-child {
        display: flex;
        justify-content: space-between;
    }
    
    &__left-parent {
        justify-content: flex-start;
    }
    
    &__right-parent {
        justify-content: flex-end;
    }
}
</style>